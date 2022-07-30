import "package:flutter/material.dart";

import 'package:flutter_svg/flutter_svg.dart';

import "package:frontend/src/colors.dart" as colors;

var title = SvgPicture.asset(
  "assets/title.svg",
  semanticsLabel: "Omega Omnibus Title",
  color: colors.primaryLight,
  alignment: Alignment.topLeft,
  height: 100,
);
