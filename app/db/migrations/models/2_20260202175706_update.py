from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "code" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "type" VARCHAR(64) NOT NULL,
    "value" VARCHAR(32) NOT NULL,
    "expires_at" TIMESTAMPTZ NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "code";"""


MODELS_STATE = (
    "eJztmF1P2zAUhv9KlSsmMQSlFLS7UIroGO0EZZtAKHITN41w7GA7lAr1v8924nw1yVoEWz"
    "v1qu35iM957PS8yavhEwcitnfLIGXGl8argYEPxZe8Y7dhgCBIzdLAwQipyDAJGTFOgc2F"
    "cQwQg8LkQGZTL+AewcKKQ4Skkdgi0MNuagqx9xRCixMX8gmkwnH/IMweduALZPpn8GiNPY"
    "icXKGeI9dWdovPAmXrYX6uAuVqI8smKPRxGhzM+ITgJNrDXFpdiCEFHMrLcxrK8mV1cZu6"
    "o6jSNCQqMZPjwDEIEc+0uyQDm2DJT1QT7YQrV/ncPGgdt04O260TEaIqSSzH86i9tPcoUR"
    "HoD4258gMOogiFMeWmPhfIdSaAlqPT8QV4ouQiPI2qjp42pPjSI/NO/HzwYiGIXT6R0I6O"
    "amj9MK87F+b1joj6JLsh4hhHh7sfu5qRTyJNEUIfeGgVhknCFmICMQCMTQktuYurOWZzti"
    "gTlDaFsmUL8EWYZ8LDPR+WA81nFpA6ceqe/rKmgEUPzgCjWfxfXMN32Lvq3gzNq++yE5+x"
    "J6QQmcOu9DSVdVaw7rQLW5FcpPGzN7xoyJ+Nu0G/qwgSxl2qVkzjhneGrAmEnFiYTC3gZM"
    "aGtmowuY0NA+eNG5vP3G7sP91YVbwUMuPHzEiWhhGwH6eAOlbOk7mzhexii3t/GqedX15D"
    "BBTXxV2OlVxHfKzn/s71odXWLCrSJFWsFl1+0y9aAAauqlquLVfK4igRvBpTtd61dcRW7m"
    "6Q3FXdryAxdPxmyot2awl10W5VigvpymuLZ4DClQAmCZtJ8LC5BMHDZiVB6So8LbwEnpgc"
    "bxji+czNHOIbMrR127VybKuz/ws5VqKzGaTWShM2k/HnMbsm+/cOk3ZBxOYZLgI8JxR6Lr"
    "6EM8WxJyoC2C6bD8UXj+sHsEqvCjMF00SzZc+G6E90BXk0M82bjnnWNebVyv8jla8JqWdP"
    "jBLtG3tq1S9IY7b6d83uyjr9+yxup/j5cGkFl6Zspob7kJds8tZYAWIcvpkAD/b3lwAooi"
    "oBKl/hLSXBHOIS6fT1ZtCvkE1pSgHkLRYN3juezXcbyGP8YT2x1lCUXefkkYa3c2X+KnLt"
    "fBucFnWPvMBp2Uz+m+Nl/huA1wtF"
)
