import "package:flutter/material.dart";
import 'package:frontend/src/components/info_page.dart';
import 'package:frontend/src/components/text.dart';

class OOContactInfo extends StatelessWidget {
  final String role;
  final String name;
  final Map<String, String>? contactInfo;

  const OOContactInfo(
      {required this.role, required this.name, this.contactInfo, Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    List<Widget> contactInfos = [];
    contactInfo?.forEach((key, value) {
      contactInfos.add(Column(
        children: [
          OOSelectableText("$key $value", size: "6"),
          const SizedBox(height: 3),
        ],
      ));
    });

    var contactInfosWidget = Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: contactInfos,
    );

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        OOText(role, size: "3", weight: "bold"),
        const SizedBox(height: 10),
        OOText(name, size: "4"),
        if (contactInfo != null) const SizedBox(height: 5),
        if (contactInfo != null) contactInfosWidget,
        const SizedBox(height: 30),
      ],
    );
  }
}

class OOContact extends StatelessWidget {
  const OOContact({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return OOInfoPage(
      "Contact",
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: const [
          OOContactInfo(
            role: "Creator",
            name: "Yann COLOMBIER",
            contactInfo: {
              "Email": "yannargenteuil@live.fr",
              "Phone": "+33 6 63 55 46 20",
              "Website": "yanncolombiergraphisme.com",
            },
          ),
          OOContactInfo(
            role: "Programmer",
            name: "Dimitri VINET",
            contactInfo: {
              "Email": "dimitri.vinet@outlook.com",
              "Phone": "+33 7 61 62 33 35",
              "Website": "dimitrivinet.com",
            },
          )
        ],
      ),
    );
  }
}
