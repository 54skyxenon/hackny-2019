// Entry.js

import React, { Component } from 'react';
import {
  Image,
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { Card } from 'react-native-elements';

import PropTypes from 'prop-types';

export default class Entry extends React.Component
{
		render()
		{
				let imageURI = this.props.pic;

				return (<Card title={this.props.name} image={{uri: imageURI}} style={styles.container}>
							    <Text>{ this.props.address }{"\n"}{this.props.price}💲, {this.props.rating} ⭐</Text>
							  </Card>);
		}
}

Entry.propTypes = {
	uid: PropTypes.string.isRequired,
	lat_long: PropTypes.string.isRequired,
	address: PropTypes.string.isRequired,
	name: PropTypes.string.isRequired,
	rating: PropTypes.string.isRequired,
	price: PropTypes.string.isRequired,
	pic: PropTypes.string.isRequired
}

const styles = StyleSheet.create({
		container: {
			flex: 1,
			flexDirection: 'row',
			alignItems:'center',
			justifyContent:'center'
		}
});
