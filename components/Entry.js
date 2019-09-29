// Entry.js

import React, { Component } from 'react';
import { Text } from 'react-native';

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
