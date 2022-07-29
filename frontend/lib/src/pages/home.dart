import "package:flutter/material.dart";
import 'package:flutter_svg/flutter_svg.dart';
import 'package:frontend/src/colors.dart';

import "../components/text.dart";

var title = SvgPicture.asset(
  "assets/title.svg",
  semanticsLabel: "Omega Omnibus Title",
  color: primaryLight,
  alignment: Alignment.topLeft,
  height: 100,
);

class OOHome extends StatelessWidget {
  const OOHome({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.only(top: 90),
      color: primaryDark,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Center(child: SizedBox(height: 100, child: title)),
          Container(
            padding: const EdgeInsets.only(left: 45),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SizedBox(height: 100),
                TextButton(
                  child: OOText("New Game"),
                  onPressed: () => Navigator.pushNamed(context, '/new_game'),
                ),
                TextButton(
                  child: OOText("History"),
                  onPressed: () => Navigator.pushNamed(context, '/history'),
                ),
                TextButton(
                  child: OOText("Stats"),
                  onPressed: () => Navigator.pushNamed(context, '/stats'),
                ),
                const SizedBox(height: 110),
                TextButton(
                  child: OOText("About"),
                  onPressed: () => Navigator.pushNamed(context, '/about'),
                ),
                const SizedBox(height: 40),
                TextButton(
                  child: OOText("Contact"),
                  onPressed: () => Navigator.pushNamed(context, '/contact'),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
