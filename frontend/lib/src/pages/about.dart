import "package:flutter/material.dart";

import 'package:url_launcher/url_launcher.dart';

import 'package:frontend/src/components/page.dart';
import 'package:frontend/src/components/text.dart';

var ooUrl = Uri.parse("https://www.github.com/dimitrivinet/omega-omnibus");

Future<void> tryLaunchUrl(Uri url) async {
  if (!await launchUrl(url)) {
    throw 'Could not launch $url';
  }
}

class OOAbout extends StatelessWidget {
  const OOAbout({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    const String aboutTextSize = "5";

    const String aboutText =
        """Omega Omnibus is an application for making playing Omnibus easier.

It takes away the hassle of counting points to let the players concentrate on the best part of the game: playing.
""";

    return OOInfoPage(
      "About",
      child: Container(
        padding: const EdgeInsets.only(right: 20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const OOText(aboutText, size: aboutTextSize),
            TextButton(
                child: const OOText("More info",
                    size: aboutTextSize, decorations: TextDecoration.underline),
                onPressed: () => tryLaunchUrl(ooUrl)),
          ],
        ),
      ),
    );
  }
}
