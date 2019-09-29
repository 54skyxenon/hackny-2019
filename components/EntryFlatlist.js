// EntryFlatlist.js

import React, { Component } from 'react';
import { FlatList, StyleSheet, Text, View } from 'react-native';

import Entry from './Entry';
import PropTypes from 'prop-types';

export default class EntryFlatlist extends React.Component
{
	render()
	{
		return (
			<FlatList
					style={styles.container}
					data={this.props.entries}
					horizontal={true}
					renderItem={({item}) => <Entry uid={item._id}
					 															lat_long={item.lat}
																				address={item.Address}
																				name={item.Name}
																				rating={item.Rating}
																				price={item.Price}
																				pic={item.Pic}
																			/>}
				/>
		);
	}
}

EntryFlatlist.propTypes = {entries: PropTypes.arrayOf(Entry)}

const styles = StyleSheet.create({
  container: {
   flex: 1
  },
  item: {
    padding: 10,
    fontSize: 15,
  },
})
