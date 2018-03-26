export interface Book {
  isbn: string;
  user: string;
  creation_date: string;

}


export interface BookList {

  count: number;
  next: string;
  previous: string;
  results: Array<Book>;
}
