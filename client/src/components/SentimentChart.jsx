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
      <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
          <CartesianGrid strokeDasharray="2 3" />
          <XAxis margin={{bottom: 30}} dataKey="name" label={{ value: "Sentiment of comments multiplied by weighted likes number", position: "insideBottom", offset: -5 }} />
          <YAxis label={{ value: "% of comments", angle: -90, position: "Left", offset: -5 }} />
          <Tooltip />
          <Legend />
          <Bar dataKey="value" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </>
  );
};
export default SentimentChart;
