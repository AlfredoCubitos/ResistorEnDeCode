import re

SI_units = {
    "-24": (-24, "y", "yocto"),
    "-21": (-21, "z", "zepto"),
    "-18": (-18, "a", "atto"),
    "-15": (-15, "f", "femto"),
    "-12": (-12, "p", "pico"),
    "-9": (-9, "n", "nano"),
    "-6": (-6, "µ", "micro"),
    "-3": (-3, "m", "milli"),
    "-2": (-2, "c", "centi"),
    "-1": (-1, "d", "deci"),
    "0": (0, "", ""),
    "1": (1, "da", "deka"),
    "2": (2, "h", "hecto"),
    "3": (3, "k", "kilo"),
    "6": (6, "M", "mega"),
    "9": (9, "G", "giga"),
    "12": (12, "T", "tera"),
    "15": (15, "P", "peta"),
    "18": (18, "E", "exa"),
    "21": (21, "Z", "zetta"),
    "24": (24, "Y", "yotta"),
    # Binary
    "10": (10, "Ki", "kibi"),
    "20": (20, "Mi", "mebi"),
    "30": (30, "Gi", "gibi"),
    "40": (40, "Ti", "tebi"),
    "50": (50, "Pi", "pebi"),
    "60": (60, "Ei", "exbi"),
    "70": (70, "Zi", "zebi"),
    "80": (80, "Yi", "yobi"),
}


def format_metric(
    value, precision=3, decimal=True, valid_prefixes=(9, 6, 3, 0, -3, -6, -9)
):
    import math

    try:
        if decimal:
            exponent = math.floor(math.log10(value))
        else:
            exponent = math.floor(math.log2(value))
    except ValueError:
        # log of 0 is -inf
        return "0 "

    # Find first prefix exponent smaller than the given exponent, in descending order.
    # Use the last good enough value if nothing was found.
    best_prefix = 0
    for prefix in sorted(valid_prefixes, reverse=True):
        best_prefix = prefix
        if prefix <= exponent:
            break

    if decimal:
        value /= 10**best_prefix
    else:
        value /= 2**best_prefix

    # Rounds the value and places a reasonable metric prefix
    format_str = "{:." + str(precision) + "}"
    value = float(format_str.format(float(value)))
    prefix = SI_units[str(int(best_prefix))][1]
    # Round off trailing decimal when possible
    if value == math.floor(value):
        value = int(value)
    # return f"{value} {prefix}"
    return (value, prefix)


def format_resistance(_value, _precision):
    # Allow the Giga, Mega, kilo, none, milli prefixes
    value_str, prefix = format_metric(_value, _precision, True, (9, 6, 3, 0, -3))
    return f"{value_str}Ω"


def edit_format_resistance(_value, _precision):
    # Allow the Giga, Mega, kilo, none, milli prefixes
    value_str, prefix = format_metric(_value, _precision, True, (9, 6, 3, 0, -3))
    # return f"{value_str}Ω"
    return value_str, prefix + "Ω"


def calculate_values(_tolerance, _mantissa, _multiplier):
    tolerance_val = float(re.match(r"\d+\.?\d*", _tolerance).group(0)) * 0.01
    actual_value = _mantissa * 10**_multiplier
    min_value = actual_value * (1 - tolerance_val)
    max_value = actual_value * (1 + tolerance_val)
    return actual_value, min_value, max_value


def get_multiplier(value):
    if len(value) <= 2:
        return {
            "multipler": "1",
            "color": "black",
            "idx": "3",
        }  # idx is the combobox index
    elif len(value) > 2 and len(value) <= 3:
        return {"multipler": "10", "color": "brown", "idx": "4"}
    elif len(value) > 3 and len(value) <= 4:
        return {"multipler": "100", "color": "red", "idx": "5"}
    elif len(value) > 4 and len(value) <= 5:  # 1k
        return {"multipler": "1000", "color": "orange", "idx": "6"}
    elif len(value) > 5 and len(value) <= 6:  # 10k
        return {"multipler": "10000", "color": "yellow", "idx": "7"}
    elif len(value) > 6 and len(value) <= 7:  # 100k
        return {"multipler": "100000", "color": "green", "idx": "8"}
    elif len(value) > 7 and len(value) <= 8:  # 1M
        return {"multipler": "1000000", "color": "blue", "idx": "9"}
    elif len(value) > 8 and len(value) <= 9:  # 10M
        return {"multipler": "10000000", "color": "purple", "idx": "10"}
    elif len(value) > 9 and len(value) <= 10:  # 100M
        return {"multipler": "100000000", "color": "gray", "idx": "11"}
    elif len(value) > 10:  # 1G
        return {"multipler": "1000000000", "color": "white", "idx": "12"}