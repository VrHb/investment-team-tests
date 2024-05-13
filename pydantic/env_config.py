from pydantic import BaseSettings, ValidationError, Field, PostgresDsn


class EnvSettings(BaseSettings):
    project_key: str
    debug: bool
    postgres_config: PostgresDsn | None

    class Config:
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'


def main() -> None:
    try:
        config = EnvSettings()
        print(config)
    except ValidationError as e:
        print(e.json())


if __name__ == '__main__':
    main()
