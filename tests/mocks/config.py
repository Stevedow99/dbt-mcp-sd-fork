from dbt_mcp.config.config import (
    Config,
    DbtCliConfig,
    DiscoveryConfig,
    RemoteConfig,
    SemanticLayerConfig,
    TrackingConfig,
)

mock_config = Config(
    tracking_config=TrackingConfig(
        prod_environment_id=1,
        dev_environment_id=1,
        dbt_cloud_user_id=1,
        local_user_id="1",
    ),
    remote_config=RemoteConfig(
        multicell_account_prefix=None,
        prod_environment_id=1,
        dev_environment_id=1,
        user_id=1,
        token="token",
        host="http://localhost/mcp",
    ),
    dbt_cli_config=DbtCliConfig(
        project_dir="/test/project",
        dbt_path="/path/to/dbt",
    ),
    discovery_config=DiscoveryConfig(
        host="localhost",
        token="token",
        multicell_account_prefix=None,
        environment_id=1,
    ),
    semantic_layer_config=SemanticLayerConfig(
        host="localhost",
        service_token="token",
        multicell_account_prefix=None,
        prod_environment_id=1,
    ),
)
