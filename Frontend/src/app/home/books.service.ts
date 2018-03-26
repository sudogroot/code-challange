import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';


const routes = {
  books: () => `/books/`
};


@Injectable()
export class BooksService {

  constructor(private httpClient: HttpClient) {
  }

  getBooksList(page: string = ''): Observable<any> {
    // let h = new HttpHeaders().set('Cookies', 'user_name=wajih')
    // {withCredentials : true}
    return this.httpClient
      .get(routes.books() + page, {withCredentials: true});
  }

}
