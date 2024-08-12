# test_game

## Dependencies
+ Python 3.10.12
+ pip 23.2.1

## Install Requirements
`pip install -r requirements.txt`

## Run(Inside venv)
`python -m game.main`

## Logging
+ Db log: `logs/db.log` (Изначально папки `logs` нет, она создается автоматически при запуске игры)
+ Логирование настроено в JSON формате
```
2024-08-06 16:49:04,777 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952144778, "msg": "Connected to: scores.db"}
2024-08-06 16:49:04,778 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952144778, "msg": "Connection closed"}
2024-08-06 16:49:05,198 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952145198, "msg": "Connected to: scores.db"}
2024-08-06 16:49:05,198 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952145199, "msg": "SELECTED from scores: [('Guest', 0), ('Guest', 0), ('Guest', 0), ('Guest', 0), ('Guest', 0), ('Guest', 21), ('Guest', 21), ('Guest', 73), ('Guest', 168), ('Guest', 200), ('Guest', 317), ('Guest', 381), ('Guest3232', 680), ('Guest', 744), ('YourNickName', 850), ('Guest434343', 1080), ('Hyuifyd', 1231), ('Guest00000', 1638), ('YourNickName', 3080)]"}
2024-08-06 16:49:05,198 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952145199, "msg": "Connection closed"}
2024-08-06 16:49:28,375 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952168374, "msg": "Connected to: scores.db"}
2024-08-06 16:49:28,377 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952168377, "msg": "Inserted Record (Guest23323, 320)"}
2024-08-06 16:49:28,379 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952168380, "msg": "Connection closed"}
2024-08-06 16:49:28,380 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952168380, "msg": "Connected to: scores.db"}
2024-08-06 16:49:28,380 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952168381, "msg": "SELECTED from scores: [('Guest', 0), ('Guest', 0), ('Guest', 0), ('Guest', 0), ('Guest', 0), ('Guest', 21), ('Guest', 21), ('Guest', 73), ('Guest', 168), ('Guest', 200), ('Guest', 317), ('Guest23323', 320), ('Guest', 381), ('Guest3232', 680), ('Guest', 744), ('YourNickName', 850), ('Guest434343', 1080), ('Hyuifyd', 1231), ('Guest00000', 1638), ('YourNickName', 3080)]"}
2024-08-06 16:49:28,380 - db - INFO - {"log_level": "INFO", "timestamp_ms": 1722952168381, "msg": "Connection closed"}
```