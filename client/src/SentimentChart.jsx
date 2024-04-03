import React, { Component } from "react";
import PropTypes from "prop-types";
import {
  BarChart,
  Bar,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const SentimentChart = ({ sentiment }) => {
    const { negative, positive } = sentiment;
  const data = [
    {
      name: "Negative",
      value: negative,
    },
    {
      name: "Positive",
      value: positive,
    },
  ];
  return (
    <>
      <h2>Sentiment Analysis Chart</h2>
      <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="value" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </>
  );
};
export default SentimentChart;
