import airbyte_cdk as cdk

class FootballDataConnector(cdk.Connector):
    """Football Data Connector."""

    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)
        self.api_token = config.get("api_token")
        self.league_code = config.get("league_code")

    def get_schema(self):
        """Gets the schema for the connector."""

        return cdk.Schema(
            tables=[
                cdk.Table(
                    name="matches",
                    columns=[
                        cdk.Column(name="id", type="INT"),
                        cdk.Column(name="date", type="DATETIME"),
                        cdk.Column(name="home_team", type="STRING"),
                        cdk.Column(name="away_team", type="STRING"),
                        cdk.Column(name="home_goals", type="INT"),
                        cdk.Column(name="away_goals", type="INT"),
                    ],
                ),
                cdk.Table(
                    name="teams",
                    columns=[
                        cdk.Column(name="id", type="INT"),
                        cdk.Column(name="name", type="STRING"),
                    ],
                ),
            ]
        )

    def get_streams(self):
        """Gets the streams for the connector."""

        return [
            cdk.Stream(
                name="matches",
                schema=self.get_schema().get_table("matches"),
            ),
            cdk.Stream(
                name="teams",
                schema=self.get_schema().get_table("teams"),
                records=self.fetch_teams(),
            ),
        ]

    def fetch_teams(self):
        """Fetches teams data from the football-data API."""

        url = f"https://api.football-data.org/v2/competitions/{self.league_code}/teams"
        headers = {"X-Auth-Token": self.api_token}
        response = requests.get(url, headers=headers)
        teams = response.json().get("teams", [])

        records = []
        for team in teams:
            records.append({
                "id": team["id"],
                "name": team["name"],
            })

        return records

    def get_source_config(self):
        """Gets the source configuration for the connector."""

        return cdk.SourceConfig(
            api_token=self.api_token,
        )

    def get_destination_config(self):
        """Gets the destination configuration for the connector."""

        return cdk.DestinationConfig()

    def get_sync_config(self):
        """Gets the sync configuration for the connector."""

        return cdk.SyncConfig(
            schedule="* * * * *",
        )
