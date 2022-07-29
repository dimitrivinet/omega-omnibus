import 'package:flutter/material.dart';
import "colors.dart" as colors;

var baseTextStyle = const TextStyle(
  fontFamily: "AtkinsonHyperlegible",
  color: colors.primaryLight,
  decoration: TextDecoration.none,
  fontWeight: FontWeight.w100,
);

class OOTheme {
  static TextTheme get white {
    return Typography.whiteCupertino;
  }

  static TextTheme get black {
    return Typography.blackCupertino;
  }
}
