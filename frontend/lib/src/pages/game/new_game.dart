import "package:flutter/material.dart";

import "package:frontend/src/colors.dart" as colors;
import "package:frontend/src/components/page.dart";
import "package:frontend/src/components/text.dart";
import "package:frontend/src/components/title.dart" as title;
import "package:frontend/src/theme.dart" as theme;

const int maxNumPlayers = 8;

class PlayerListState {
  static void addPlayer() {}

  static TextField addPlayerField = const TextField(
    decoration: InputDecoration(
        border: OutlineInputBorder(), hintText: "New player name"),
  );

  static TextButton addPlayerButton =
      const TextButton(onPressed: addPlayer, child: OOText("Add player"));
}

class OONewGame extends StatefulWidget {
  const OONewGame({Key? key}) : super(key: key);
  @override
  State<OONewGame> createState() => _OONewGameState();
}

class _OONewGameState extends State<OONewGame> {
  late String currentText;
  late TextField addPlayerField;
  late TextButton addPlayerButton;
  late List<String> playerNames;
  late List<Widget> playerList;
  late List<Widget> playerListBase;

  final fieldText = TextEditingController();

  _OONewGameState() {
    currentText = "";

    addPlayerField = TextField(
      controller: fieldText,
      decoration: InputDecoration(
          border: const OutlineInputBorder(),
          hintText: "New player name",
          hintStyle: theme.baseTextStyle),
      onChanged: (text) => currentText = text,
      onSubmitted: (text) => addPlayer(text: text),
    );

    addPlayerButton =
        TextButton(onPressed: addPlayer, child: const OOText("Add player"));

    playerNames = [];
    playerList = [addPlayerField, addPlayerButton];
  }

  void addPlayer({String? text}) {
    if (currentText == "") return;

    if (text != null) currentText = text;

    setState(() {
      playerNames.add(currentText);
      playerList.insert(playerList.length - 1, OOText(currentText));
      currentText = "";
      fieldText.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    return OOBasePage(
      Container(
        padding: const EdgeInsets.only(top: 10),
        color: colors.primaryDark,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Center(child: SizedBox(height: 100, child: title.title)),
            const SizedBox(height: 100),
            ListView.builder(
              shrinkWrap: true,
              itemBuilder: (context, index) =>
                  playerList.length - 2 == maxNumPlayers
                      ? playerList[index + 1]
                      : playerList[index],
              itemCount: playerList.length - 2 == maxNumPlayers
                  ? maxNumPlayers
                  : playerList.length,
            ),
          ],
        ),
      ),
    );
  }
}
