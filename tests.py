from bot import Bot


def test_tweet_cycle():
    bot = Bot()

    # send a random tweet
    post_status = bot.random_tweet(send=True)

    # fetch the most recent tweet
    last_status, = bot.api.user_timeline(count=1)

    # make sure the ids are the same
    assert post_status.id == last_status.id
