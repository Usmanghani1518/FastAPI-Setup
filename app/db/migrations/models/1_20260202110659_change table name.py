from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
        DROP TABLE IF EXISTS "user";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "users";"""


MODELS_STATE = (
    "eJztlmtr2zAUhv+K8acOutJm6YV9c7OMZizJaNNttBSjWIojIkuuJC8NJf99OvLdudCMQV"
    "vIp9jveY91ziM7Os9uJDBh6uhWEancz86zy1FEzEU9cOi4KI5LGQSNxsw6k8IyVlqiQBtx"
    "gpgiRsJEBZLGmgpuVJ4wBqIIjJHysJQSTh8T4msREj0l0gTuH4xMOSZPROW38cyfUMJwrV"
    "CKYW2r+3oRW63H9VdrhNXGfiBYEvHSHC/0VPDCTbkGNSScSKQJPF7LBMqH6rI2847SSktL"
    "WmIlB5MJSpiutPtCBoHgwM9Uk+5ECKt8bJ20z9sXn87aF8ZiKymU82XaXtl7mmgJDEbu0s"
    "aRRqnDYiy52d8Vcp0pkuvR5f4GPFNyE16Oahu9XCjxla/Mf+IXoSefER7qKUA7Pd1C66d3"
    "3bnyrg+M6wN0I8xrnL7cgyzUSmOAtERIIkTZLgyLhD3EAmKMlJoLueYr3syxmrNHWaAMJI"
    "GWfaRXYX4xEU0jsh5oPbOBFGepR/nFGwVsesBDzhbZf/EWvqNev3sz8vo/oJNIqUdmEXmj"
    "LkRaVl001IOzxlYUD3F+9UZXDtw6d8NB1xIUSofSrlj6Rncu1IQSLXwu5j7ClWMjV3MwtY"
    "1NYvyPG1vP3G/sq26sLR4GmcmsciSDMEbBbI4k9lcioiU2eVdDUStqKoij0O4KsIUqs8HO"
    "I5IG03UjXxbZOvOh0rMf+t7R0PfHjOpQ0g5nbSVlf9QWIOHT2AFiZn+fAE+Oj18A0Lg2Ar"
    "SxxqwiuCZ8zXn27WY42DCklCkNkLfcNHiPaaAPHUaVfnibWLdQhK5rZ1YO76Dv/W5y7Xwf"
    "XjYPI3jApWH8qsfL8i8yJTKG"
)
