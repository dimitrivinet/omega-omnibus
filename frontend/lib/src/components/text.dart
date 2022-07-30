import "package:flutter/material.dart";

import "package:frontend/src/theme.dart" as theme;

const Map<String, double> sizes = {
  "1": 56.0,
  "2": 48.0,
  "3": 36.0,
  "4": 30.0,
  "5": 26.0,
  "6": 18.0,
  "7": 14.0,
};

const Map<String, FontWeight> weights = {
  "normal": FontWeight.normal,
  "bold": FontWeight.bold,
};

class OOText extends StatelessWidget {
  final String data;
  final String size;
  final String weight;
  final TextDecoration decorations;

  TextStyle getStyle() {
    return theme.baseTextStyle.copyWith(
        fontSize: sizes[size],
        fontWeight: weights[weight],
        decoration: decorations);
  }

  const OOText(
    this.data, {
    this.size = "3",
    this.weight = "normal",
    this.decorations = TextDecoration.none,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Text(
      data,
      style: getStyle(),
    );
  }
}

class OOSelectableText extends OOText {
  const OOSelectableText(
    String data, {
    String size = "3",
    String weight = "normal",
    TextDecoration decorations = TextDecoration.none,
    Key? key,
  }) : super(data,
            size: size, weight: weight, decorations: decorations, key: key);

  @override
  Widget build(BuildContext context) {
    return SelectableText(
      data,
      style: getStyle(),
    );
  }
}
