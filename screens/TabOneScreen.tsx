import React, { useState } from "react";
import { StyleSheet } from "react-native";
import { HStack, Stack, Center, NativeBaseProvider } from "native-base";
import PokeList from "../components/PokeList";
// import { useState } from 'react';
import EditScreenInfo from "../components/EditScreenInfo";
import { Text, View } from "../components/Themed";
export const pokeDataLarge = require("../data/poke-data-large.json");

const pokeData = require("../data/pokemon-info-small.json");

export default function TabOneScreen() {
  const [data, setData] = useState(pokeData);
  console.log("data here: ", data);
  const typeList = data["type-list"];
  console.log("type-list: ", typeList);

  return (
    <View style={styles.container}>
      <Stack space={3} alignItems="center">
        {/* <Heading>HStack</Heading> */}
        <HStack space={3} alignItems="center">
          <Center
            size={24}
            bg="primary.400"
            rounded="md"
            _text={{
              color: "white",
            }}
            shadow={3}
          >
            Box 1
          </Center>
          <Center
            bg="secondary.400"
            size={24}
            rounded="md"
            _text={{
              color: "white",
            }}
            shadow={3}
          >
            Box 2
          </Center>
          <Center
            size={24}
            bg="emerald.400"
            rounded="md"
            _text={{
              color: "white",
            }}
            shadow={3}
          >
            Box 3
          </Center>
        </HStack>
      </Stack>
      <View
        style={styles.separator}
        lightColor="#eee"
        darkColor="rgba(255,255,255,0.1)"
      />
      {/* <EditScreenInfo path="/screens/TabOneScreen.tsx" /> */}
      {/* <Text> */}
      {/* {typeList.map(type => <Text key={type.toString()}> {type["resistant-to"].map(weakness => {weakness},)}</Text>)} */}
      {/* <ListTypes typeList={typeList} /> */}
      <PokeList />
      {/* </Text> */}
    </View>
  );
}

function ListTypes({ typeList }) {
  console.log("ListTypes: ", typeList);
  const typeListLength = typeList.length;
  console.log("typeList LEngth: ", typeListLength);
  // typeList.map((type, i) => console.log(i, type));
  const components = typeList.map(
    (type, i) => (
      // console.log("typer: ", type.type))
      console.log(type), (<PokeType key={i} pokeName={type.type}></PokeType>)
    )
  );
  console.log(components);
  return <View>{components}</View>;
}

function PokeType({ pokeName }) {
  console.log("props: ");
  console.log("name: ", pokeName);
  return (
    <View>
      <Text>Type {pokeName}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
  },
});
