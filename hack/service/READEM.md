
## prepare

```
$ sudo ln -s (this repository top) /opt/eaecm
$ vi /etc/eaecm.conf
```

/etc/eaecm.conf

```
CRAM_HOST=XXXX
CRAM_PORT=XXXX
CRAM_TOKEN=XXXX
```

```
cp eaecm.service /etc/systemd/system
```
