import * as React from 'react';
import { StyleSheet } from 'react-native';
import { HStack, Stack, Center, NativeBaseProvider } from "native-base";
import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';

export default function TabOneScreen() {
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

      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <EditScreenInfo path="/screens/TabOneScreen.tsx" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
