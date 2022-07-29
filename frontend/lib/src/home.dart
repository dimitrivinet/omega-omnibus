import "package:flutter/material.dart";
import 'package:flutter_svg/flutter_svg.dart';
import 'package:frontend/src/colors.dart';

import "theme.dart";

var title = SvgPicture.asset(
  "title.svg",
  semanticsLabel: "Omega Omnibus Title",
  color: primaryLight,
  alignment: Alignment.topLeft,
);

class OOHome extends StatelessWidget {
  const OOHome({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(100),
      color: primaryDark,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(height: 200, child: title),
          const SizedBox(height: 100),
          const OOText("New Game"),
          const OOText("History"),
          const OOText("Stats"),
          const SizedBox(height: 100),
          const OOText("About"),
          const OOText("Contact"),
        ],
      ),
    );
  }
}
