# k12outreachboston

A site for collecting volunteering opportunities for college students in Boston.

## development

```shell
docker-compose up -d --build
docker-compose exec django /src/setup.sh
```

The initial superuser account is `admin` / `qWg62vtWTuSoS3eqzwKUL9ZQPwsfeH` and you can get to the webapp at http://localhost:8000.

## TODO
   - set up lets encrypt for https
   - convert google doc spreadsheet to fixture and import with `setup.sh`
   - start building user-facing site
