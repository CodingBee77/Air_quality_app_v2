from app.models import CurrentMeasurement, ChartMeasurement, StandardFactors
from app.mappers.obj_mapper import ObjectMapper
from app.config import settings
from app.airly_client.client import AirlyClient

API_RESPONSE = {
  "current": {
    "fromDateTime": "2021-10-18T09:06:35.404Z",
    "tillDateTime": "2021-10-18T10:06:35.404Z",
    "values": [
      {
        "name": "PM1",
        "value": 16.66
      },
      {
        "name": "PM25",
        "value": 24.54
      },
      {
        "name": "PM10",
        "value": 39.67
      },
      {
        "name": "PRESSURE",
        "value": 1025.07
      },
      {
        "name": "HUMIDITY",
        "value": 91.12
      },
      {
        "name": "TEMPERATURE",
        "value": 8.51
      }
    ],
    "indexes": [
      {
        "name": "AIRLY_CAQI",
        "value": 40.9,
        "level": "LOW",
        "description": "Well... It's been better.",
        "advice": "The air is nice and clean today!",
        "color": "#D1CF1E"
      }
    ],
    "standards": [
      {
        "name": "WHO",
        "pollutant": "PM25",
        "limit": 25,
        "percent": 98.17,
        "averaging": "24h"
      },
      {
        "name": "WHO",
        "pollutant": "PM10",
        "limit": 50,
        "percent": 79.34,
        "averaging": "24h"
      }
    ]
  },
  "history": [
    {
      "fromDateTime": "2021-10-17T10:00:00.000Z",
      "tillDateTime": "2021-10-17T11:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 3.8
        },
        {
          "name": "PM25",
          "value": 6.03
        },
        {
          "name": "PM10",
          "value": 8.82
        },
        {
          "name": "PRESSURE",
          "value": 1022.11
        },
        {
          "name": "HUMIDITY",
          "value": 72.13
        },
        {
          "name": "TEMPERATURE",
          "value": 10.56
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 10.05,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Catch your breath!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 24.11,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 17.63,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T11:00:00.000Z",
      "tillDateTime": "2021-10-17T12:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 5.81
        },
        {
          "name": "PM25",
          "value": 8.23
        },
        {
          "name": "PM10",
          "value": 11.96
        },
        {
          "name": "PRESSURE",
          "value": 1021.75
        },
        {
          "name": "HUMIDITY",
          "value": 64.67
        },
        {
          "name": "TEMPERATURE",
          "value": 12.22
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 13.72,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Enjoy life!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 32.92,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 23.92,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T12:00:00.000Z",
      "tillDateTime": "2021-10-17T13:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 5.36
        },
        {
          "name": "PM25",
          "value": 7.76
        },
        {
          "name": "PM10",
          "value": 11.37
        },
        {
          "name": "PRESSURE",
          "value": 1021.17
        },
        {
          "name": "HUMIDITY",
          "value": 62.06
        },
        {
          "name": "TEMPERATURE",
          "value": 12.5
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 12.93,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "It couldn't be better ;)",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 31.03,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 22.74,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T13:00:00.000Z",
      "tillDateTime": "2021-10-17T14:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 6.45
        },
        {
          "name": "PM25",
          "value": 8.9
        },
        {
          "name": "PM10",
          "value": 12.93
        },
        {
          "name": "PRESSURE",
          "value": 1020.95
        },
        {
          "name": "HUMIDITY",
          "value": 61.14
        },
        {
          "name": "TEMPERATURE",
          "value": 12.37
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 14.83,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Catch your breath!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 35.59,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 25.86,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T14:00:00.000Z",
      "tillDateTime": "2021-10-17T15:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 7.97
        },
        {
          "name": "PM25",
          "value": 11.44
        },
        {
          "name": "PM10",
          "value": 16.6
        },
        {
          "name": "PRESSURE",
          "value": 1020.77
        },
        {
          "name": "HUMIDITY",
          "value": 61.08
        },
        {
          "name": "TEMPERATURE",
          "value": 12.11
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 19.07,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Breathe deep! The air is clean!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 45.76,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 33.19,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T15:00:00.000Z",
      "tillDateTime": "2021-10-17T16:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 8.38
        },
        {
          "name": "PM25",
          "value": 12.08
        },
        {
          "name": "PM10",
          "value": 18.04
        },
        {
          "name": "PRESSURE",
          "value": 1021.05
        },
        {
          "name": "HUMIDITY",
          "value": 67.32
        },
        {
          "name": "TEMPERATURE",
          "value": 10.93
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 20.13,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Zero dust - zero worries!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 48.31,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 36.07,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T16:00:00.000Z",
      "tillDateTime": "2021-10-17T17:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 9.71
        },
        {
          "name": "PM25",
          "value": 14.14
        },
        {
          "name": "PM10",
          "value": 20.83
        },
        {
          "name": "PRESSURE",
          "value": 1021.5
        },
        {
          "name": "HUMIDITY",
          "value": 71.32
        },
        {
          "name": "TEMPERATURE",
          "value": 9.91
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 23.57,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Dear me, how wonderful!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 56.56,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 41.67,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T17:00:00.000Z",
      "tillDateTime": "2021-10-17T18:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 10.83
        },
        {
          "name": "PM25",
          "value": 15.62
        },
        {
          "name": "PM10",
          "value": 23.04
        },
        {
          "name": "PRESSURE",
          "value": 1021.61
        },
        {
          "name": "HUMIDITY",
          "value": 78.68
        },
        {
          "name": "TEMPERATURE",
          "value": 8.5
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 26.04,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Do you smell it? That's the smell of clean air. :)",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 62.49,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 46.07,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T18:00:00.000Z",
      "tillDateTime": "2021-10-17T19:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 13.99
        },
        {
          "name": "PM25",
          "value": 20.42
        },
        {
          "name": "PM10",
          "value": 31.26
        },
        {
          "name": "PRESSURE",
          "value": 1021.7
        },
        {
          "name": "HUMIDITY",
          "value": 83.04
        },
        {
          "name": "TEMPERATURE",
          "value": 8.09
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 34.03,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Enjoy the clean air.",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 81.67,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 62.53,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T19:00:00.000Z",
      "tillDateTime": "2021-10-17T20:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 16.02
        },
        {
          "name": "PM25",
          "value": 23.21
        },
        {
          "name": "PM10",
          "value": 36.92
        },
        {
          "name": "PRESSURE",
          "value": 1021.96
        },
        {
          "name": "HUMIDITY",
          "value": 85
        },
        {
          "name": "TEMPERATURE",
          "value": 7.65
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 38.68,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "The air quality is good today!",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 92.82,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 73.84,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T20:00:00.000Z",
      "tillDateTime": "2021-10-17T21:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 16.51
        },
        {
          "name": "PM25",
          "value": 24.45
        },
        {
          "name": "PM10",
          "value": 39.25
        },
        {
          "name": "PRESSURE",
          "value": 1022.24
        },
        {
          "name": "HUMIDITY",
          "value": 85.83
        },
        {
          "name": "TEMPERATURE",
          "value": 7.22
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 40.75,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Enjoy the clean air.",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 97.81,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 78.49,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T21:00:00.000Z",
      "tillDateTime": "2021-10-17T22:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 17.9
        },
        {
          "name": "PM25",
          "value": 26.32
        },
        {
          "name": "PM10",
          "value": 42.53
        },
        {
          "name": "PRESSURE",
          "value": 1022.18
        },
        {
          "name": "HUMIDITY",
          "value": 88.05
        },
        {
          "name": "TEMPERATURE",
          "value": 6.91
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 43.87,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Take a deep breath. Today, you can. ;)",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 105.28,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 85.05,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T22:00:00.000Z",
      "tillDateTime": "2021-10-17T23:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 18.15
        },
        {
          "name": "PM25",
          "value": 26.83
        },
        {
          "name": "PM10",
          "value": 43.52
        },
        {
          "name": "PRESSURE",
          "value": 1022.2
        },
        {
          "name": "HUMIDITY",
          "value": 89.74
        },
        {
          "name": "TEMPERATURE",
          "value": 6.55
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 44.72,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Take a deep breath. Today, you can. ;)",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 107.33,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 87.04,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-17T23:00:00.000Z",
      "tillDateTime": "2021-10-18T00:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 18.7
        },
        {
          "name": "PM25",
          "value": 27.76
        },
        {
          "name": "PM10",
          "value": 45.06
        },
        {
          "name": "PRESSURE",
          "value": 1022.35
        },
        {
          "name": "HUMIDITY",
          "value": 90.51
        },
        {
          "name": "TEMPERATURE",
          "value": 6.23
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 46.27,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Do you smell it? That's the smell of clean air. :)",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 111.05,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 90.12,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T00:00:00.000Z",
      "tillDateTime": "2021-10-18T01:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 20.4
        },
        {
          "name": "PM25",
          "value": 30.11
        },
        {
          "name": "PM10",
          "value": 49.66
        },
        {
          "name": "PRESSURE",
          "value": 1022.35
        },
        {
          "name": "HUMIDITY",
          "value": 90.25
        },
        {
          "name": "TEMPERATURE",
          "value": 6.15
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 50.11,
          "level": "MEDIUM",
          "description": "The air quality is average.",
          "advice": "It's better to limit your outside physical activity today.",
          "color": "#EFBB0F"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 120.43,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 99.31,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T01:00:00.000Z",
      "tillDateTime": "2021-10-18T02:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 22.31
        },
        {
          "name": "PM25",
          "value": 32.92
        },
        {
          "name": "PM10",
          "value": 54.54
        },
        {
          "name": "PRESSURE",
          "value": 1022.27
        },
        {
          "name": "HUMIDITY",
          "value": 89.67
        },
        {
          "name": "TEMPERATURE",
          "value": 6.03
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 52.92,
          "level": "MEDIUM",
          "description": "The air quality is average.",
          "advice": "Neither good nor bad. Think before leaving the house.",
          "color": "#EFBB0F"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 131.67,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 109.09,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T02:00:00.000Z",
      "tillDateTime": "2021-10-18T03:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 25.17
        },
        {
          "name": "PM25",
          "value": 36.76
        },
        {
          "name": "PM10",
          "value": 60.01
        },
        {
          "name": "PRESSURE",
          "value": 1022.18
        },
        {
          "name": "HUMIDITY",
          "value": 91.75
        },
        {
          "name": "TEMPERATURE",
          "value": 6.09
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 56.76,
          "level": "MEDIUM",
          "description": "The air quality is average.",
          "advice": "Things were good once... Let's hope it doesn't get worse!",
          "color": "#EFBB0F"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 147.05,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 120.01,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T03:00:00.000Z",
      "tillDateTime": "2021-10-18T04:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 25.88
        },
        {
          "name": "PM25",
          "value": 37.8
        },
        {
          "name": "PM10",
          "value": 60.86
        },
        {
          "name": "PRESSURE",
          "value": 1022.26
        },
        {
          "name": "HUMIDITY",
          "value": 93.39
        },
        {
          "name": "TEMPERATURE",
          "value": 6.01
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 57.8,
          "level": "MEDIUM",
          "description": "The air quality is average.",
          "advice": "Watch out - a few signs of smog today.",
          "color": "#EFBB0F"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 151.2,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 121.72,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T04:00:00.000Z",
      "tillDateTime": "2021-10-18T05:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 25.44
        },
        {
          "name": "PM25",
          "value": 36.95
        },
        {
          "name": "PM10",
          "value": 60.08
        },
        {
          "name": "PRESSURE",
          "value": 1022.56
        },
        {
          "name": "HUMIDITY",
          "value": 96.48
        },
        {
          "name": "TEMPERATURE",
          "value": 6.07
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 56.95,
          "level": "MEDIUM",
          "description": "The air quality is average.",
          "advice": "The air is slightly polluted.",
          "color": "#EFBB0F"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 147.78,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 120.16,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T05:00:00.000Z",
      "tillDateTime": "2021-10-18T06:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 22.95
        },
        {
          "name": "PM25",
          "value": 33.85
        },
        {
          "name": "PM10",
          "value": 56.11
        },
        {
          "name": "PRESSURE",
          "value": 1023.2
        },
        {
          "name": "HUMIDITY",
          "value": 94.2
        },
        {
          "name": "TEMPERATURE",
          "value": 6.56
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 53.85,
          "level": "MEDIUM",
          "description": "The air quality is average.",
          "advice": "Try to stay with your family at home.",
          "color": "#EFBB0F"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 135.4,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 112.22,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T06:00:00.000Z",
      "tillDateTime": "2021-10-18T07:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 21.08
        },
        {
          "name": "PM25",
          "value": 31.22
        },
        {
          "name": "PM10",
          "value": 51.51
        },
        {
          "name": "PRESSURE",
          "value": 1023.89
        },
        {
          "name": "HUMIDITY",
          "value": 92.67
        },
        {
          "name": "TEMPERATURE",
          "value": 6.88
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 51.22,
          "level": "MEDIUM",
          "description": "The air quality is average.",
          "advice": "Something's hanging in the air. Take care!",
          "color": "#EFBB0F"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 124.86,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 103.03,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T07:00:00.000Z",
      "tillDateTime": "2021-10-18T08:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 19.82
        },
        {
          "name": "PM25",
          "value": 29.23
        },
        {
          "name": "PM10",
          "value": 47.75
        },
        {
          "name": "PRESSURE",
          "value": 1024.41
        },
        {
          "name": "HUMIDITY",
          "value": 93.25
        },
        {
          "name": "TEMPERATURE",
          "value": 7.23
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 48.72,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Enjoy the clean air.",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 116.92,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 95.51,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T08:00:00.000Z",
      "tillDateTime": "2021-10-18T09:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 18.55
        },
        {
          "name": "PM25",
          "value": 27.59
        },
        {
          "name": "PM10",
          "value": 44.77
        },
        {
          "name": "PRESSURE",
          "value": 1024.85
        },
        {
          "name": "HUMIDITY",
          "value": 92.91
        },
        {
          "name": "TEMPERATURE",
          "value": 7.73
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 45.98,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Take a breath!",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 110.36,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 89.54,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T09:00:00.000Z",
      "tillDateTime": "2021-10-18T10:00:00.000Z",
      "values": [
        {
          "name": "PM1",
          "value": 16.94
        },
        {
          "name": "PM25",
          "value": 24.98
        },
        {
          "name": "PM10",
          "value": 40.51
        },
        {
          "name": "PRESSURE",
          "value": 1025.05
        },
        {
          "name": "HUMIDITY",
          "value": 91.34
        },
        {
          "name": "TEMPERATURE",
          "value": 8.44
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 41.63,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "The air is nice and clean today!",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 99.91,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 81.02,
          "averaging": "24h"
        }
      ]
    }
  ],
  "forecast": [
    {
      "fromDateTime": "2021-10-18T10:00:00.000Z",
      "tillDateTime": "2021-10-18T11:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 20.72
        },
        {
          "name": "PM10",
          "value": 39.17
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 39.17,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Do you smell it? That's the smell of clean air. :)",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 82.9,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 78.34,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T11:00:00.000Z",
      "tillDateTime": "2021-10-18T12:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 18.07
        },
        {
          "name": "PM10",
          "value": 34.95
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 34.95,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Enjoy the clean air.",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 72.27,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 69.9,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T12:00:00.000Z",
      "tillDateTime": "2021-10-18T13:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 16.06
        },
        {
          "name": "PM10",
          "value": 32.45
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 32.45,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Enjoy the clean air.",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 64.26,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 64.9,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T13:00:00.000Z",
      "tillDateTime": "2021-10-18T14:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 14.98
        },
        {
          "name": "PM10",
          "value": 31.16
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 31.16,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Enjoy the clean air.",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 59.9,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 62.32,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T14:00:00.000Z",
      "tillDateTime": "2021-10-18T15:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 14.71
        },
        {
          "name": "PM10",
          "value": 32.53
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 32.53,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Do you smell it? That's the smell of clean air. :)",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 58.86,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 65.05,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T15:00:00.000Z",
      "tillDateTime": "2021-10-18T16:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 14.35
        },
        {
          "name": "PM10",
          "value": 32.37
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 32.37,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Don't miss this day! The clean air calls!",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 57.39,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 64.73,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T16:00:00.000Z",
      "tillDateTime": "2021-10-18T17:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 14.34
        },
        {
          "name": "PM10",
          "value": 32.91
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 32.91,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "Don't miss this day! The clean air calls!",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 57.38,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 65.83,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T17:00:00.000Z",
      "tillDateTime": "2021-10-18T18:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 14.34
        },
        {
          "name": "PM10",
          "value": 32.93
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 32.93,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "The air is nice and clean today!",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 57.34,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 65.86,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T18:00:00.000Z",
      "tillDateTime": "2021-10-18T19:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 14.16
        },
        {
          "name": "PM10",
          "value": 31.82
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 31.82,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "The air quality is good today!",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 56.64,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 63.63,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T19:00:00.000Z",
      "tillDateTime": "2021-10-18T20:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 13.05
        },
        {
          "name": "PM10",
          "value": 30.3
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 30.3,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "The air quality is good today!",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 52.2,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 60.6,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T20:00:00.000Z",
      "tillDateTime": "2021-10-18T21:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 11.13
        },
        {
          "name": "PM10",
          "value": 27.22
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 27.22,
          "level": "LOW",
          "description": "Well... It's been better.",
          "advice": "The air quality is good today!",
          "color": "#D1CF1E"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 44.5,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 54.43,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T21:00:00.000Z",
      "tillDateTime": "2021-10-18T22:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 9.88
        },
        {
          "name": "PM10",
          "value": 24.23
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 24.23,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Breathe as much as you can!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 39.52,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 48.47,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T22:00:00.000Z",
      "tillDateTime": "2021-10-18T23:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 8.35
        },
        {
          "name": "PM10",
          "value": 20.96
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 20.96,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "The air is great!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 33.4,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 41.92,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-18T23:00:00.000Z",
      "tillDateTime": "2021-10-19T00:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 7.12
        },
        {
          "name": "PM10",
          "value": 18.6
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 18.6,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Enjoy life!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 28.49,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 37.2,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T00:00:00.000Z",
      "tillDateTime": "2021-10-19T01:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 6.76
        },
        {
          "name": "PM10",
          "value": 16.72
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 16.72,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Perfect air for exercising! Go for it!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 27.04,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 33.44,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T01:00:00.000Z",
      "tillDateTime": "2021-10-19T02:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 6.31
        },
        {
          "name": "PM10",
          "value": 15.46
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 15.46,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "It couldn't be better ;)",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 25.22,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 30.93,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T02:00:00.000Z",
      "tillDateTime": "2021-10-19T03:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 7.66
        },
        {
          "name": "PM10",
          "value": 16.29
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 16.29,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Green equals clean!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 30.64,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 32.59,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T03:00:00.000Z",
      "tillDateTime": "2021-10-19T04:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 9.94
        },
        {
          "name": "PM10",
          "value": 18.27
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 18.27,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Breathe as much as you can!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 39.75,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 36.55,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T04:00:00.000Z",
      "tillDateTime": "2021-10-19T05:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 11.6
        },
        {
          "name": "PM10",
          "value": 19.96
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 19.96,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "It couldn't be better ;)",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 46.39,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 39.93,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T05:00:00.000Z",
      "tillDateTime": "2021-10-19T06:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 12.02
        },
        {
          "name": "PM10",
          "value": 21.07
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 21.07,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Enjoy life!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 48.09,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 42.14,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T06:00:00.000Z",
      "tillDateTime": "2021-10-19T07:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 11.37
        },
        {
          "name": "PM10",
          "value": 22.06
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 22.06,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Green equals clean!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 45.48,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 44.11,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T07:00:00.000Z",
      "tillDateTime": "2021-10-19T08:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 9.78
        },
        {
          "name": "PM10",
          "value": 22.98
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 22.98,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Perfect air for exercising! Go for it!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 39.12,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 45.96,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T08:00:00.000Z",
      "tillDateTime": "2021-10-19T09:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 7.74
        },
        {
          "name": "PM10",
          "value": 23.68
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 23.68,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "Breathe deeply!",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 30.97,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 47.35,
          "averaging": "24h"
        }
      ]
    },
    {
      "fromDateTime": "2021-10-19T09:00:00.000Z",
      "tillDateTime": "2021-10-19T10:00:00.000Z",
      "values": [
        {
          "name": "PM25",
          "value": 5.84
        },
        {
          "name": "PM10",
          "value": 24.37
        }
      ],
      "indexes": [
        {
          "name": "AIRLY_CAQI",
          "value": 24.37,
          "level": "VERY_LOW",
          "description": "Great air here today!",
          "advice": "It couldn't be better ;)",
          "color": "#6BC926"
        }
      ],
      "standards": [
        {
          "name": "WHO",
          "pollutant": "PM25",
          "limit": 25,
          "percent": 23.37,
          "averaging": "24h"
        },
        {
          "name": "WHO",
          "pollutant": "PM10",
          "limit": 50,
          "percent": 48.74,
          "averaging": "24h"
        }
      ]
    }
  ]
}


class MeasurementRepository:
    def __init__(self):
        pass


    def get_current_measurement_by_coordinates(self, lat: float, long: float) -> CurrentMeasurement:
        # api_response = AirlyClient.get_measurement(lat, long)
        # print(api_request)
        api_response = API_RESPONSE
        mapper = ObjectMapper()
        current_measurement = mapper.map_current_measurement(api_response)
        return current_measurement


    def get_chart_measurement_by_coordinates(self, lat: float, long: float, data_type: str) -> ChartMeasurement:
          # api_response = AirlyClient.get_measurement(lat, long)
        api_response = API_RESPONSE
        # print(api_request)
        mapper = ObjectMapper()
        historic_measurement = mapper.map_chart_measurement(response=api_response, data_type=data_type)
        return historic_measurement


    def get_standards_by_coordinates(self, lat: float, long: float) -> StandardFactors:
        # api_response = AirlyClient.get_measurement(lat, long)
        api_response = API_RESPONSE
        # print(api_request)
        mapper = ObjectMapper()
        standards = mapper.map_standard_factor(response=api_response)
        return standards
