# Base Configuration
|    Name    | Type |Default|
|------------|------|-------|
|LUME_BACKEND|string|local  |


# Model Database
|                  Name                  | Type  |Default|
|----------------------------------------|-------|-------|
|LUME_MODEL_DB__HOST                     |string |       |
|LUME_MODEL_DB__PORT                     |integer|       |
|LUME_MODEL_DB__USER                     |string |       |
|LUME_MODEL_DB__PASSWORD                 |string |       |
|LUME_MODEL_DB__DATABASE                 |string |       |
|LUME_MODEL_DB__CONNECTION__POOL_SIZE    |integer|       |
|LUME_MODEL_DB__CONNECTION__POOL_PRE_PING|boolean|True   |


# Results Database
|                  Name                  | Type  |Default|
|----------------------------------------|-------|-------|
|LUME_MODEL_DB__HOST                     |string |       |
|LUME_MODEL_DB__PORT                     |integer|       |
|LUME_MODEL_DB__USER                     |string |       |
|LUME_MODEL_DB__PASSWORD                 |string |       |
|LUME_MODEL_DB__DATABASE                 |string |       |
|LUME_MODEL_DB__CONNECTION__POOL_SIZE    |integer|       |
|LUME_MODEL_DB__CONNECTION__POOL_PRE_PING|boolean|True   |


# Scheduling Service
|              Name              | Type  |           Default           |
|--------------------------------|-------|-----------------------------|
|LUME_PREFECT__SERVER__TAG       |string |core-1.2.4                   |
|LUME_PREFECT__SERVER__HOST      |string |http://localhost             |
|LUME_PREFECT__SERVER__HOST_PORT |string |4200                         |
|LUME_PREFECT__SERVER__HOST_IP   |string |127.0.0.1                    |
|LUME_PREFECT__UI__HOST          |string |http://localhost             |
|LUME_PREFECT__UI__HOST_PORT     |string |8080                         |
|LUME_PREFECT__UI__HOST_IP       |string |127.0.0.1                    |
|LUME_PREFECT__UI__APOLLO_URL    |string |http://localhost:4200/graphql|
|LUME_PREFECT__TELEMETRY__ENABLED|boolean|True                         |
|LUME_PREFECT__AGENT__HOST       |string |http://localhost             |
|LUME_PREFECT__AGENT__HOST_PORT  |string |5000                         |
|LUME_PREFECT__HOME_DIR          |string |~/.prefect                   |
|LUME_PREFECT__DEBUG             |boolean|False                        |
|LUME_PREFECT__BACKEND           |string |server                       |