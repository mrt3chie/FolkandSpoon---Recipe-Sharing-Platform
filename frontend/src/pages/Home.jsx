import React from "react";
import ReceipeCard from "../components/ReceipeCard";
import recipes from "../dataDummy/recipe";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="mt-10">
      <h2 className="text-center text-2xl font-bold mb-10">All Recipes</h2>
      <div className="grid grid-cols-3 lg:grid-cols-4 gap-4">
        {recipes.map((recipe) => (
          <Link to={`/recipe/${recipe.id}`}>
            <ReceipeCard
              key={recipe.id}
              title={recipe.title}
              imgUrl={recipe.imgURL}
              createdAt={recipe.createdAt}
              userName={recipe.Username}
            />
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Home;
