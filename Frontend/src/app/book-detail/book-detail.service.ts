import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';

const routes = {
  bookDetail: (isbn: string) => '/books/' + isbn + '/',
  postComment: (isbn: string) => '/books/' + isbn + '/comments/',
  postStars: (isbn: string) => '/books/' + isbn + '/stars/'
};


@Injectable()
export class BookDetailService {

  constructor(private httpClient: HttpClient) {
  }

  getBookDetail(isbn: string): Observable<any> {
    return this.httpClient
      .get(routes.bookDetail(isbn));
  }

  postComment(isbn: string, comment: string): Observable<any> {
    return this.httpClient
      .post(routes.postComment(isbn), {content: comment}, {withCredentials: true});
  }

  postStars(isbn: string, stars: number): Observable<any> {
    return this.httpClient
      .post(routes.postStars(isbn), {stars: stars}, {withCredentials: true});
  }

}
