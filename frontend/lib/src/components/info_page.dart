import "package:flutter/material.dart";

import "../colors.dart" as colors;
import "back_button.dart";
import "text.dart";

class OOInfoPage extends StatelessWidget {
  final String title;
  final Widget child;

  const OOInfoPage(this.title, {Key? key, required this.child})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: colors.primaryDark,
      appBar: AppBar(
        shadowColor: colors.primaryDark,
        backgroundColor: colors.primaryDark,
        elevation: 0,
        leading: const OOBackButton(colors.primaryLight, colors.primaryDark),
      ),
      body: Container(
        padding: const EdgeInsets.only(top: 90),
        color: colors.primaryDark,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
                padding: const EdgeInsets.only(left: 50),
                child: OOText(title, size: "1")),
            const SizedBox(height: 50),
            Container(padding: const EdgeInsets.only(left: 40), child: child),
          ],
        ),
      ),
    );
  }
}
