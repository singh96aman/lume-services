import pytest 
from pytest_mysql import factories
from sqlalchemy import create_engine
from string import Template

import mongomock

from lume_services.data.model.db.mysql import MySQLConfig, MySQLService
from lume_services.data.model.model_db_service import ModelDBService
from lume_services.data.results.db.service import DBServiceConfig
from lume_services.data.results.db.mongodb.service import MongodbService
from lume_services.data.results.results_db_service import ResultsDBService

from lume_services.data.results.db.mongodb.models import ModelDocs

mysql_server = factories.mysql_proc()


def pytest_addoption(parser):

    parser.addini(
        "mysql_user", default="root", help="MySQL user"
    )

    parser.addini(
        "mysql_database", default="model_db", help="Model database name"
    )

    parser.addini(
        "mysql_poolsize", default=1, help="MySQL client poolsize"
    )


@pytest.fixture(scope="session", autouse=True)
def mysql_user(request):
    return request.config.getini("mysql_user")

@pytest.fixture(scope="session", autouse=True)
def mysql_host(request):
    return request.config.getini("mysql_host")


@pytest.fixture(scope="session", autouse=True)
def mysql_port(request):
    return int(request.config.getini("mysql_port"))


@pytest.fixture(scope="session", autouse=True)
def mysql_database(request):
    return request.config.getini("mysql_database")


@pytest.fixture(scope="session", autouse=True)
def mysql_pool_size(request):
    return int(request.config.getini("mysql_poolsize"))


@pytest.fixture(scope="session", autouse=True)
def base_db_uri(mysql_user, mysql_host, mysql_port):
    return Template("mysql+pymysql://${user}:@${host}:${port}").substitute(user=mysql_user, host=mysql_host, port=mysql_port)


@pytest.fixture(scope="session", autouse=True)
def mysql_config(mysql_user, mysql_host, mysql_port, mysql_database, mysql_pool_size):

    db_uri = Template("mysql+pymysql://${user}:@${host}:${port}/${database}").substitute(user=mysql_user, host=mysql_host, port=mysql_port, database=mysql_database)

    return MySQLConfig(
        db_uri=db_uri,
        pool_size=mysql_pool_size,
    )


@pytest.mark.usefixtures("mysql_proc")
@pytest.fixture(scope="module", autouse=True)
def mysql_service(mysql_config):
    mysql_service = MySQLService(mysql_config)
    return mysql_service


@pytest.mark.usefixtures("mysql_proc")
@pytest.fixture(scope="module", autouse=True)
def model_db_service(mysql_service, mysql_database, base_db_uri, mysql_proc):

    # start the mysql process if not started
    if not mysql_proc.running():
        mysql_proc.start()

    engine = create_engine(base_db_uri, pool_size=1)
    with engine.connect() as connection:
        connection.execute("CREATE DATABASE IF NOT EXISTS model_db;")

    model_db_service = ModelDBService(mysql_service)
    model_db_service.apply_schema()

    # set up database
    yield model_db_service

    with engine.connect() as connection:
        connection.execute(f"DROP DATABASE {mysql_database};")


class MongomockResultsDBConfig(DBServiceConfig):
    host: str= 'mongomock://localhost'
    db: str= "localhost"
    port: int = 27017


@pytest.fixture(scope="session", autouse=True)
def mongodb_config():
    return MongomockResultsDBConfig()

@mongomock.patch(servers=(('localhost', 27017),))
@pytest.fixture(scope="module", autouse=True)
def mongodb_service(mongodb_config):
    return MongodbService(mongodb_config)


@pytest.fixture(scope="module", autouse=True)
def results_db_service(mongodb_service):

    results_db_service = ResultsDBService(mongodb_service, ModelDocs)

    # no teardown needed because mock is module scoped
    return results_db_service
import pytest
from datetime import datetime

@pytest.fixture(scope="session", autouse=True)
def test_generic_result_document():
    return  {
        "flow_id": "test_flow_id",
        "inputs": {
            "input1": 2.0,
            "input2": [1,2,3,4,5],
            "input3": "my_file.txt"
        },
        "outputs": {
            "output1": 2.0,
            "output2": [1,2,3,4,5],
            "ouptut3": "my_file.txt"
        },
    }


@pytest.fixture(scope="module", autouse=True)
def test_impact_result_document():
    return  {
        "flow_id": "test_flow_id",
        "inputs": {
            "input1": 2.0,
            "input2": [1,2,3,4,5],
            "input3": "my_file.txt"
        },
        "outputs": {
            "output1": 2.0,
            "output2": [1,2,3,4,5],
            "ouptut3": "my_file.txt"
        },
        "plot_file": "my_plot_file.txt",
        "archive": "archive_file.txt",
        "pv_collection_isotime": datetime.now(),
        "config": {
            "config1": 1,
            "config2": 2
        }
    }