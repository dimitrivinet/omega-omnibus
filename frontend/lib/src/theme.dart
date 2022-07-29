import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import "colors.dart" as colors;

var baseTextStyle = const TextStyle(
  // fontFamily: "AtkinsonHyperlegible",
  color: colors.primaryLight,
  decoration: TextDecoration.none,
);

class OOText extends StatelessWidget {
  final String data;

  const OOText(
    this.data, {
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Text(data, style: baseTextStyle);
  }
}

class OOTheme {
  static ThemeData get theme {
    TextTheme baseTextTheme = const TextTheme();
    baseTextTheme = GoogleFonts.anekBanglaTextTheme(baseTextTheme);
    baseTextTheme = baseTextTheme.apply(
      bodyColor: const Color.fromARGB(255, 254, 237, 159),
    );

    return ThemeData(textTheme: baseTextTheme);
  }
}
