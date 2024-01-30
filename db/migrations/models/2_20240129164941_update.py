from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "logmessage" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "message" TEXT NOT NULL  /* 日志消息 */
);
        ALTER TABLE "player" ADD "online" INT NOT NULL  DEFAULT 0 /* 玩家是否在线 */;
        CREATE TABLE IF NOT EXISTS "siteconfig" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "key" VARCHAR(100) NOT NULL UNIQUE /* 配置名称 */,
    "value_str" VARCHAR(255) NOT NULL  /* 配置值 */,
    "type" VARCHAR(100) NOT NULL  /* 值的类型 */
) /* 一些配置，主要用于定时任务的一些配置 */;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "player" DROP COLUMN "online";
        DROP TABLE IF EXISTS "logmessage";
        DROP TABLE IF EXISTS "siteconfig";"""
