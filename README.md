# FootballDataConnector

FootballDataConnector is an Airbyte connector designed to fetch football data from the [football-data](https://www.football-data.org/) API. It allows you to retrieve information about matches and teams for a specific league's ongoing season. The connector is configurable, enabling you to fetch data for different leagues by simply modifying the configuration.

## Task Description

1. Installation: Install Airbyte on your computer following the [instructions](https://docs.airbyte.com/deploying-airbyte/local-deployment/)
2. Airbyte and CDK: Familiarize yourself with [Airbyte](https://docs.airbyte.com/) and the Airbyte Connector Development Kit [CDK](https://docs.airbyte.com/connector-development/cdk-python/).
3. Connector Implementation: Implement a connector using Airbyte CDK to fetch data from the [football-data API](https://www.football-data.org/).

## Connector Features

- Fetch Teams and Matches: Retrieve teams and matches for an ongoing season of a specific league.
- Configurable League Selection: Change the league by modifying the connector configuration.
- Rate Limit Consideration: Be mindful of the API's rate limit of max 10 calls per minute. More details [here](https://www.football-data.org/pricing).

## Installation

```bash
git clone https://github.com/JanneImmonen/FootballDataConnector.git
cd FootballDataConnector
pip install -r requirements.txt
```

## Configuration

Create a YAML configuration file with the following details:

- API key from the football-data.org website
- League code for the desired competition
- Destination details
- Schedule for the sync job

api_key: YOUR_API_KEY
streams:
  - matches
  - league_tables
  - player_statistics
destination:
  type: postgres
  host: YOUR_HOST
  port: YOUR_PORT
  database: YOUR_DATABASE
  user: YOUR_USERNAME
  password: YOUR_PASSWORD
schedule:
  cron: '0 0 * * *'

## Usage

1. Create a sync job in Airbyte.
2. Select the "Football Data Connector" and specify the configuration file.
3. Start the sync job to import data into the specified destination.

## Supported Streams

- Matches: Includes match ID, date, home team, away team, home goals, and away goals.
- Teams: Includes team ID and name.

## Documentation

For more information, please refer to the following documentation:

[Airbyte Documentation](https://docs.airbyte.com/)

[Football-Data.org Documentation](https://www.football-data.org/)

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
