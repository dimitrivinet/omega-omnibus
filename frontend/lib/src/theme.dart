import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

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
