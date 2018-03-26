export interface Stars {
  stars: number;
  user: string;
  creation_date: string;
}

export interface Comments {

  content: string;
  user: string;
  creation_date: string;
}

export interface BookDetail {
  creation_date: string;
  comments: Array<Comments>;
  title: string;
  user: string;
  isbn: string;
  stars: Array<Stars>;
  avg_rating: number;

}
