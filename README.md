# Hefeng_weather Skill for Claude

[![smithery badge](https://smithery.ai/badge/@ZhangYouJie-Major/hefeng_weather)](https://smithery.ai/server/@ZhangYouJie-Major/hefeng_weather)

Hefeng_weather is a powerful skill designed for Anthropic's Claude that makes use of the Model Context Protocol (MCP). It seamlessly interacts with the Hefeng Weather API and offers numerous commands, enabling Claude to provide precise and prompt weather-related information.

## Features

- **Current Weather**: Know real-time atmospheric conditions in any city across the globe, including temperature, humidity, visibility, precipitation, and more.
  
- **Weather Forecasts**: Get comprehensive predictions for upcoming weather patterns in any location worldwide.

- **Life Indices**: Understand how the weather might influence daily activities, covering warnings on UV, allergen levels, attire, and more.

- **Astronomical Data**: Obtain extensive come-uppance on anytime celestial insights.

- **Air Quality**: Vigilantly observes the air condition realms, offering insights on AQI, pollution intensity and health-related recommendations for outdoor endeavours.

- **Meteorological Warnings**: Provides advisory and cautionary alerts regarding looming weather adversities.

## Installing via Smithery

To install Hefeng Weather for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@ZhangYouJie-Major/hefeng_weather):

```bash
npx -y @smithery/cli install @ZhangYouJie-Major/hefeng_weather --client claude
```

## Interface Overview

All operations are conducted via method calls over MCP with structured JSON responses. The skill primarily relies on two categories – resources and tools.

### Resources

The skill propagates meaningful information by integrating data from the Hefeng Weather API.

### Tools

The skill offers a slew of callable functionalities based on user queries:

1. **Current Weather**: `getCurrentWeather` method which accepts a location (longitude and latitude) to offer current atmospheric conditions.

2. **Weather Forecast**: `getWeatherForecast` method which returns anticipated weather transgressions for a provided location over a specified duration.

3. **Life Indices**: `getLifeIndex` method delivering life indices reliant on the given location.

4. **Astronomical Data**: `getAstroData` method which shares celestial insights for stipulated dates and location.

5. **Air Quality Index**: `getAQIData` method for retelling air quality quotient for a chosen location.

6. **Meteorological Alerts**: `getAlerts` method notifying warnings over possible meteorological threats and adversities.

## Configuration

Upon integrating the Hefeng Weather skill to Claude, users will need the following:

- API Key set up for Hefeng Weather API.
- Adequately adjust the API request intervals adhering to Hefeng Weather API restrictions to avoid pitfalls.

## Contribution

The Hefeng Weather skill is open-source and thrives on community inputs. Contributions, suggestions and feature requests are always welcome.

## Licensing

Distributed under the MIT License.