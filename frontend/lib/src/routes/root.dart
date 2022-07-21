import 'package:flutter/material.dart';

class RootPage extends StatelessWidget {
  const RootPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
        alignment: Alignment.center,
        color: const Color.fromARGB(255, 1, 4, 38),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("\u{03A9}",
                style: DefaultTextStyle.of(context)
                    .style
                    .apply(fontSizeFactor: 3.0)),
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const <Text>[Text("mega"), Text("mnibus")],
            )
          ],
        ));
  }
}
