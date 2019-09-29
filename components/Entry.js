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

export default class Entry extends React.Component
{
		propTypes = {
			uid: PropTypes.string.isRequired,
			name: PropTypes.string.isRequired,
			lat: PropTypes.number.isRequired,
			long: PropTypes.number.isRequired,
			address: PropTypes.string.isRequired,
			rating: PropTypes.number.isRequired
		}

		render()
		{
				return (<Text>Hello World! | </Text>);
		}
}
