import React from "react";
import { StyleSheet, View, Text } from "react-native";
import { List, Container, Box, ScrollView, Image } from "native-base";
import { pokeDataLarge } from "../screens/TabOneScreen";
import Bug from "../assets/icons/bug.svg";
import Dark from "../assets/icons/dark.svg";
import Dragon from "../assets/icons/dragon.svg";
import Electric from "../assets/icons/electric.svg";
import Fairy from "../assets/icons/fairy.svg";
import Fighting from "../assets/icons/fighting.svg";
import Fire from "../assets/icons/fire.svg";
import Flying from "../assets/icons/flying.svg";
import Ghost from "../assets/icons/ghost.svg";
import Grass from "../assets/icons/grass.svg";
import Ground from "../assets/icons/ground.svg";
import Ice from "../assets/icons/ice.svg";
import Normal from "../assets/icons/normal.svg";
import Poison from "../assets/icons/poison.svg";
import Psychic from "../assets/icons/psychic.svg";
import Rock from "../assets/icons/rock.svg";
import Steel from "../assets/icons/steel.svg";

var whoseThatPokemonImagePath = "../assets/images/whos-that-pikachu.png";

console.log("whose that pikachuImagePath: ", whoseThatPokemonImagePath);
export default function PokeList() {
  
  return (
    <View
      style={{
        width: "80%",
        height: "65%",
      }}
    >
      <ScrollView>
        <View style={{ flexDirection: "row", justifyContent: "space-evenly" }}>
          <Bug height={11} width={11} />
          <Dark height={11} width={11} />
          <Dragon height={11} width={11} />
          <Electric height={11} width={11} />
          <Fairy height={11} width={11} />
          <Fighting height={11} width={11} />
          <Fire height={11} width={11} />
          <Flying height={11} width={11} />
          <Ghost height={11} width={11} />
          <Grass height={11} width={11} />
          <Ground height={11} width={11} />
          <Ice height={11} width={11} />
          <Normal height={11} width={11} />
          <Poison height={11} width={11} />
          <Psychic height={11} width={11} />
          <Rock height={11} width={11} />
          <Steel height={11} width={11} />
        </View>
        <List
          style={{
            flexDirection: "row",
            flexWrap: "wrap",
            justifyContent: "center",
          }}
        >
          {pokeDataLarge.map(({ name, sprites }, i) => {
            return (
              <View
                style={{
                  alignItems: "center",
                  justifyContent: "center",
                  margin: 10,
                }}
              >
                <Box bg="">
                  <Image
                    size={"sm"}
                    alt={`imagine ${name}`}
                    source={{ uri: sprites }}
                    defaultSource={require(whoseThatPokemonImagePath)}
                  ></Image>
                </Box>
                <Text style={styles.text}>{name}</Text>
              </View>
            );
          })}
        </List>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  text: {
    color: "white",
    flexWrap: "nowrap",
  },
});
