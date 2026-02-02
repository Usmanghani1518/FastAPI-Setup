from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlmtr2zAUhv+K8acOutJm6YV9c7OMZizJaNNttBSjWIojIkuuJC8NJf99OvLdudCMQV"
    "vIp9jveY91ziM7Os9uJDBh6uhWEel+dp5djiJiLmr6oeOiOC5VEDQaM2tMcsdYaYkCbbQJ"
    "YooYCRMVSBprKrhRecIYiCIwRsrDUko4fUyIr0VI9NTWcf9gZMoxeSIqv41n/oQShmtlUg"
    "xrW93Xi9hqPa6/WiOsNvYDwZKIl+Z4oaeCF27KNagh4UQiTeDxWiZQPlSXdZl3lFZaWtIS"
    "KzmYTFDCdKXdFzIIBAd+phplGwxhlY+tk/Z5++LTWfvCWGwlhXK+TNsre08TLYHByF3aON"
    "IodViMJTf7u0KuM0VyPbrc34BnSm7Cy1Fto5cLJb7ylflP/CL05DPCQz0FaKenW2j99K47"
    "V971gXF9gG6EeY3Td3uQhVppDJCWCEmEKNuFYZGwh1hAjJFScyHXfMWbOVZz9igLlIEk0L"
    "KP9CrMLyaiaUTWA61nNpDiLPUov3ijgE0PeMjZIvsv3sJ31Ot3b0Ze/wd0Ein1yCwib9SF"
    "SMuqi4Z6cNbYiuIhzq/e6MqBW+duOOhagkLpUNoVS9/ozoWaUKKFz8XcR7hybORqDqa2sU"
    "mM/3Fj65n7jX3VjbXFwyAzmVWOZBDGKJjNkcT+SkS0xCbvaihqRU0FcRTaXQG2UGU21nlE"
    "0mC6buDLIltHPlR69kPfOxr6/hCpoKQdztpKyv6oLUDCp7EDxMz+PgGeHB+/AKBxbQRoY4"
    "1ZRXBN+Jrz7NvNcLBhSClTGiBvuWnwHtNAHzqMKv3wNrFuoQhd186sHN5B3/vd5Nr5Prxs"
    "HkbwgEvD+FWPl+VfQ18xLQ=="
)
