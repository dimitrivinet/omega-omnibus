import "package:flutter/material.dart";

import "package:frontend/src/colors.dart" as colors;
import "package:frontend/src/components/page.dart";
import "package:frontend/src/components/text.dart";
import "package:frontend/src/components/title.dart" as title;
import "package:frontend/src/theme.dart" as theme;

import 'dart:developer';

const int maxNumPlayers = 8;

String capitalize(String s) =>
    s[0].toUpperCase() + s.substring(1).toLowerCase();

class OONewGame extends StatefulWidget {
  const OONewGame({Key? key}) : super(key: key);
  @override
  State<OONewGame> createState() => _OONewGameState();
}

class _OONewGameState extends State<OONewGame> {
  final fieldText = TextEditingController();

  late String currentText;
  late Container addPlayerField;
  late TextButton addPlayerButton;
  late List<String> playerNames;
  late List<Widget> playerList;
  late List<Widget> playerListBase;

  _OONewGameState() {
    currentText = "";

    addPlayerField = Container(
      child: TextField(
        controller: fieldText,
        cursorColor: colors.primaryLight,
        decoration: InputDecoration(
            enabledBorder: const UnderlineInputBorder(
                borderSide: BorderSide(color: colors.primaryLight)),
            hintText: "New player name",
            hintStyle: const OOText("", size: "5").getStyle()),
        style: const OOText("", size: "5").getStyle(),
        maxLength: 50,
        onChanged: (text) => currentText = text,
        onSubmitted: (text) => addPlayer(text: text),
      ),
    );

    addPlayerButton = TextButton(
        onPressed: addPlayer, child: const OOText("Add player", size: "5"));

    playerNames = [];
    playerList = [];
    addButtons();
  }

  void addButtons() {
    playerList.insert(0, addPlayerField);
    playerList.insert(1, addPlayerButton);
  }

  void removeButtons() {
    List<int> toRemove = [];

    for (var i = 0; i < playerList.length; i++) {
      if (playerList[i] is! OOText) {
        toRemove.add(i);
      }
    }

    for (var item in toRemove.reversed) {
      playerList.removeAt(item);
    }
  }

  void addPlayer({String? text}) {
    if (currentText == "") return;

    if (text != null) currentText = text;

    currentText = capitalize(currentText);

    var newPlayerName = OOText(currentText, size: "5");

    setState(() {
      playerNames.add(currentText);
      playerList.add(newPlayerName);
      currentText = "";
      fieldText.clear();

      if (playerList.length - 2 >= maxNumPlayers) removeButtons();
    });
  }

  @override
  Widget build(BuildContext context) {
    return OOBasePage(
      Container(
        padding: const EdgeInsets.only(top: 10, left: 20, right: 20),
        color: colors.primaryDark,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Center(child: SizedBox(height: 100, child: title.title)),
            const SizedBox(height: 100),
            ListView.builder(
              shrinkWrap: true,
              itemBuilder: (context, index) {
                if (playerList[index] is! OOText) return playerList[index];

                return TextButton(
                  style: TextButton.styleFrom(
                      padding: const EdgeInsets.only(top: 0, bottom: 0)),
                  onPressed: () {
                    setState(() {
                      playerList.removeAt(index);
                      if (playerList.length == maxNumPlayers - 1) {
                        addButtons();
                      }
                    });
                  },
                  child: Align(
                      alignment: Alignment.centerLeft,
                      child: playerList[index]),
                );
              },
              itemCount: playerList.length,
            ),
            const Spacer(),
            Align(
                alignment: Alignment.bottomRight,
                child: Container(
                  padding: const EdgeInsets.only(bottom: 20, right: 20),
                  child: TextButton(
                    onPressed: () => showDialog<String>(
                      context: context,
                      builder: (BuildContext context) => AlertDialog(
                        title: const Text("Start game"),
                        content: const Text("Do you want to start the game ?"),
                        actions: <Widget>[
                          TextButton(
                            onPressed: () => Navigator.pop(context, "Cancel"),
                            child: const Text("Cancel"),
                          ),
                          TextButton(
                            onPressed: () => Navigator.pop(context, "OK"),
                            child: const Text("Start game"),
                          ),
                        ],
                      ),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: const [
                        OOText("Play ", size: "5"),
                        Icon(
                          Icons.arrow_forward,
                          color: colors.primaryLight,
                        ),
                      ],
                    ),
                  ),
                ))
          ],
        ),
      ),
    );
  }
}
