"""Formati datuma i brojeva: dd.mm.gggg, 24-časovno vreme."""

DATE_FORMAT = "d.m.Y"
SHORT_DATE_FORMAT = "d.m.Y"
DATETIME_FORMAT = "d.m.Y H:i"
SHORT_DATETIME_FORMAT = "d.m.Y H:i"
TIME_FORMAT = "H:i"
MONTH_DAY_FORMAT = "d.m."
YEAR_MONTH_FORMAT = "m.Y"
FIRST_DAY_OF_WEEK = 1  # ponedeljak

DATE_INPUT_FORMATS = ["%d.%m.%Y", "%d.%m.%y", "%Y-%m-%d"]
DATETIME_INPUT_FORMATS = ["%d.%m.%Y %H:%M", "%d.%m.%Y %H:%M:%S", "%Y-%m-%d %H:%M"]

DECIMAL_SEPARATOR = ","
THOUSAND_SEPARATOR = "."
NUMBER_GROUPING = 3
