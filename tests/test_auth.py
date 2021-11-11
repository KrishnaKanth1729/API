import pytest

from httpx import AsyncClient
from pytest_mock import MockerFixture
from api.versions.v1.routers.auth.helpers import get_redirect, SCOPES


@pytest.mark.asyncio
async def test_redirect_default_code(app: AsyncClient):
    res = await app.get("/api/v1/auth/discord/redirect", allow_redirects=False)
    assert res.status_code == 307


@pytest.mark.asyncio
async def test_redirect_default_url(app: AsyncClient):
    res = await app.get("/api/v1/auth/discord/redirect", allow_redirects=False)
    assert res.headers.get("Location") == get_redirect(
        callback="http://127.0.0.1:8000/api/v1/auth/discord/callback",
        scopes=SCOPES,
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "callback,status",
    [("okand", 422), ("", 422)],
)
async def test_redirect_invalid_callback(app: AsyncClient, callback, status):
    res = await app.get(f"/api/v1/auth/discord/redirect?callback={callback}")
    assert res.status_code == status


@pytest.mark.asyncio
async def test_redirect_valid_callback_url(app: AsyncClient):
    res = await app.get("/api/v1/auth/discord/redirect?callback=https://twtcodejam.net")
    assert str(res.url) == get_redirect(
        callback="https://twtcodejam.net",
        scopes=SCOPES,
    )


@pytest.mark.asyncio
async def test_callback_discord_error(app: AsyncClient, mocker: MockerFixture):
    async def exchange_code(**kwargs):
        return {"error": "internal server error"}, 500

    mocker.patch("api.versions.v1.routers.auth.routes.exchange_code", new=exchange_code)

    res = await app.post(
        "/api/v1/auth/discord/callback",
        json={"code": "okand", "callback": "https://twtcodejam.net"},
    )

    assert res.status_code == 502


@pytest.mark.asyncio
async def test_callback_invalid_code(app: AsyncClient, mocker: MockerFixture):
    async def exchange_code(**kwargs):
        return {"error": 'invalid "code" in request'}, 400

    mocker.patch("api.versions.v1.routers.auth.routes.exchange_code", new=exchange_code)
    res = await app.post(
        "/api/v1/auth/discord/callback",
        json={"code": "okand", "callback": "https://twtcodejam.net"},
    )

    assert res.json() == {
        "error": "Bad Request",
        "data": (await exchange_code())[0],
        "message": "Discord returned 400 status.",
    }


@pytest.mark.asyncio
@pytest.mark.db
async def test_callback_success(app: AsyncClient, db, mocker: MockerFixture):
    async def exchange_code(**kwargs):
        return {
            "expires_in": 69420,
            "access_token": "super_doper_secret_token",
            "refresh_token": "super_doper_doper_secret_token",
        }, 200

    async def get_user(**kwargs):
        return {
            "id": 1,
            "username": "Test2",
            "avatar": "avatar",
            "discriminator": "0001",
        }

    mocker.patch("api.versions.v1.routers.auth.routes.get_user", new=get_user)
    mocker.patch("api.versions.v1.routers.auth.routes.exchange_code", new=exchange_code)

    res = await app.post(
        "/api/v1/auth/discord/callback",
        json={"code": "okand", "callback": "https://twtcodejam.net"},
    )

    assert res.status_code == 200

    await db.execute("DELETE FROM users WHERE id = 1")
