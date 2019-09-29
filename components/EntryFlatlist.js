// EntryFlatlist.js

import React, { Component } from 'react';
import { FlatList, StyleSheet, Text, View } from 'react-native';

export default class EntryFlatlist extends React.Component
{
	propTypes = {entries: PropTypes.array.isRequired}

	render()
	{
		return (
			<View style={styles.container}>
				<FlatList
					data={this.props.entries}
					renderItem={({item}) => <Text style={styles.item}>{item.name}</Text>}
				/>
			</View>
		);
	}
}

const styles = StyleSheet.create({
  container: {
   flex: 1,
   paddingTop: 22
  },
  item: {
    padding: 10,
    fontSize: 18,
    height: 44,
  },
})
