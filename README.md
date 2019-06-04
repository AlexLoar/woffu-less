This simple utility connects to [Woffu](https://www.woffu.com/en) and check-in for you.

Example of use with cron:

```
# m h  dom mon dow   command
55 7 * * 1-5 ~/woffu.py --action entrada
30 17 * * 1-4 ~/woffu.py --action salida
00 14 * * 5 ~/woffu.py --action salida
```
