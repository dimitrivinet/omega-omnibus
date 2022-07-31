import "package:flutter/material.dart";
import 'package:frontend/src/colors.dart';

import "package:frontend/src/components/text.dart";
import "package:frontend/src/components/title.dart" as title;

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
          Center(child: SizedBox(height: 100, child: title.title)),
          Container(
            padding: const EdgeInsets.only(left: 45),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SizedBox(height: 100),
                TextButton(
                  child: const OOText("New Game"),
                  onPressed: () => Navigator.pushNamed(context, '/new_game'),
                ),
                TextButton(
                  child: const OOText("History"),
                  onPressed: () => Navigator.pushNamed(context, '/history'),
                ),
                TextButton(
                  child: const OOText("Stats"),
                  onPressed: () => Navigator.pushNamed(context, '/stats'),
                ),
                const SizedBox(height: 110),
                TextButton(
                  child: const OOText("About"),
                  onPressed: () => Navigator.pushNamed(context, '/about'),
                ),
                const SizedBox(height: 40),
                TextButton(
                  child: const OOText("Contact"),
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
