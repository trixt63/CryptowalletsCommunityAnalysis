import os

from dotenv import load_dotenv

load_dotenv()


# class ArangoDBConfig:
#     HOST = os.environ.get("ARANGODB_HOST", '0.0.0.0')
#     PORT = os.environ.get("ARANGODB_PORT", '8529')
#     USERNAME = os.environ.get("ARANGODB_USERNAME", "root")
#     PASSWORD = os.environ.get("ARANGODB_PASSWORD", "dev123")

#     CONNECTION_URL = os.getenv("ARANGODB_CONNECTION_URL") or f"arangodb@{USERNAME}:{PASSWORD}@http://{HOST}:{PORT}"

#     DATABASE = os.getenv('ARANGODB_DATABASE', 'klg_database')
#     GRAPH = 'KnowledgeGraph'


# class ArangoDBLendingConfig:
#     HOST = os.environ.get("ARANGODB_LENDING_HOST", '0.0.0.0')
#     PORT = os.environ.get("ARANGODB_LENDING_PORT", '8529')
#     USERNAME = os.environ.get("ARANGODB_LENDING_USERNAME", "root")
#     PASSWORD = os.environ.get("ARANGODB_LENDING_PASSWORD", "dev123")
#
#     CONNECTION_URL = os.getenv("ARANGODB_LENDING_CONNECTION_URL") \
#                      or f"arangodb@{USERNAME}:{PASSWORD}@http://{HOST}:{PORT}"
#
#     DATABASE = 'klg_database'
#     GRAPH = 'knowledge_graph'

# class PostgresDBConfig:
#     SCHEMA = os.environ.get("POSTGRES_SCHEMA", "public")
#     TRANSFER_EVENT_TABLE = os.environ.get("POSTGRES_TRANSFER_EVENT_TABLE", "transfer_event")
#     CONNECTION_URL = os.environ.get("POSTGRES_CONNECTION_URL", "postgresql://user:password@localhost:5432/database")


# class BlockchainETLConfig:
#     HOST = os.getenv("BLOCKCHAIN_ETL_HOST")
#     PORT = os.getenv("BLOCKCHAIN_ETL_PORT")
#     USERNAME = os.getenv("BLOCKCHAIN_ETL_USERNAME")
#     PASSWORD = os.getenv("BLOCKCHAIN_ETL_PASSWORD")

#     CONNECTION_URL = os.getenv("BLOCKCHAIN_ETL_CONNECTION_URL") or f"mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}"
#     DATABASE = 'blockchain_etl'
#     DB_PREFIX = os.getenv("DB_PREFIX")


class MongoDBConfig:
    CONNECTION_URL = os.getenv("MONGODB_CONNECTION_URL")
    DATABASE = os.getenv("MONGODB_DATABASE")


# class MongoDBEntityConfig:
#     CONNECTION_URL = os.getenv("MONGODB_ENTITY_CONNECTION_URL")
#     DATABASE = os.getenv("MONGODB_ENTITY_DATABASE", "knowledge_graph")

# class MongoLendingConfig:
#     HOST = os.getenv("MONGO_LENDING_HOST")
#     PORT = os.getenv("MONGO_LENDING_PORT")
#     USERNAME = os.getenv("MONGO_LENDING_USERNAME")
#     PASSWORD = os.getenv("MONGO_LENDING_PASSWORD")
#
#     CONNECTION_URL = os.getenv("MONGO_LENDING_CONNECTION_URL") or f"mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}"
#     DATABASE = 'LendingPools'
