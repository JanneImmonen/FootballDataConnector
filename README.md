# FootballDataConnector

This connector allows you to import football data from the [football-data](https://www.football-data.org/) API into Airbyte. The data includes match results, league tables, and player statistics.

To use the connector, you will need to create an API key from the Football-Data.org website. Once you have created an API key, you can configure the connector with your API key.

The connector supports the following streams:

- Matches
- League Tables
- Player Statistics

To use the connector, you will need to create a sync job in Airbyte. The sync job will specify the streams that you want to import, the destination that you want to import to, and the schedule for the sync job.

## Installation

To install the connector, you will need to clone the repository and install the dependencies.

```bash
git clone https://github.com/JanneImmonen/FootballDataConnector.git
cd FootballDataConnector
pip install -r requirements.txt
```

## Configuration

To configure the connector, you will need to create a configuration file. The configuration file is a YAML file that specifies the following:

- The API key from the football-data.org website
- The streams that you want to import
- The destination that you want to import to
- The schedule for the sync job
- The following is an example configuration file:

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

To use the connector, you will need to create a sync job in Airbyte. The sync job will specify the configuration file that you created in the previous step.

To create a sync job, you will need to go to the Airbyte web UI and click on the "Sync Jobs" tab. Then, click on the "Create Sync Job" button. In the "Create Sync Job" dialog, select the "Football Data Connector" connector and specify the configuration file that you created.

Once you have created the sync job, you can start the sync job by clicking on the "Start" button. The sync job will import the data from the Football-Data.org API into the destination that you specified in the configuration file.

Documentation
For more information, please refer to the following documentation:

[Airbyte Documentation](https://docs.airbyte.com/)
[Football-Data.org Documentation](https://www.football-data.org/)

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
