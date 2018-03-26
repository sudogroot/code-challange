import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';



const routes = {
  books: () => `/books/`
};


@Injectable()
export class NewBookService {

  constructor(private httpClient: HttpClient) {
  }

  postNewBook(newBook: any): Observable<any> {

    return this.httpClient
      .post(routes.books(), newBook, {withCredentials: true})
  }

}
