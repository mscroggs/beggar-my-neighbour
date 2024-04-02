from mastodon import Mastodon


def toot(text):
    mdon = Mastodon(
        access_token="mastodon.secret", api_base_url="https://mathstodon.xyz")

    mdon.status_post(text)
